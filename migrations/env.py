import sys
from logging.config import fileConfig
from geoalchemy2 import alembic_helpers
from sqlalchemy import engine_from_config, pool
from alembic import context
from src.core.database import SQLALCHEMY_DATABASE_URL
from src.core.models import Base


def custom_include_obj(obj, name, obj_type, reflected, compare_to):
    if (obj_type == "table" or obj_type == "index") and (
        name.startswith("county_")
            or name.startswith("zip_")
            or name.startswith("direction_")
            or name.startswith("pagc_")
            or name.startswith("idx_tiger")
            or name.startswith("countysub_")
            or name.startswith("cousub")
            or name.startswith("addrfeat")
            or name.startswith("idx_addrfeat")
            or name.startswith("geocode_")
            or name.startswith("street_")
            or name.startswith("state_")
            or name.startswith("idx_edges")
            or name.startswith("place_")
            or name.startswith("loader_")
            or name.startswith("tiger_")
            or name.startswith("tabblock")
            or name.startswith("secondary_unit")
            or name == "addr"
            or name == "layer"
            or name == "edges"
            or name == "features"
            or name == "county"
            or name == "place"
            or name == "topology"
            or name == "bg"
            or name == "featnames"
            or name == "faces"
            or name == "state"
            or name == "tract"
            or name == "zcta5"
    ) or not alembic_helpers.include_object(obj, name, obj_type, reflected, compare_to):
        return False
    return True


sys.path.append("..")


# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here for 'autogenerate' support
target_metadata = Base.metadata

config.set_main_option('sqlalchemy.url', SQLALCHEMY_DATABASE_URL)


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        include_object=custom_include_obj,
        process_revision_directives=alembic_helpers.writer,
        render_item=alembic_helpers.render_item,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            include_object=custom_include_obj,
            process_revision_directives=alembic_helpers.writer,
            render_item=alembic_helpers.render_item,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
