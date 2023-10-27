from ..core.models import CyclingFeatureRevision
from sqlalchemy.orm import Session
from .fetch_latest_version import OpenCyclingFeaturesVersion
from datetime import datetime


def get_revision_by_external_id(db: Session, external_id: str) -> CyclingFeatureRevision:
    return db.query(CyclingFeatureRevision).filter(CyclingFeatureRevision.external_id == external_id).first()


def create_revision(db: Session, version: OpenCyclingFeaturesVersion) -> CyclingFeatureRevision:
    revision = CyclingFeatureRevision(
        external_id=version.external_id,
        url=version.url,
        date_refreshed=datetime.utcnow()
    )

    db.add(revision)
    db.commit()
    db.refresh(revision)

    return revision
