from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

# Define the SQLAlchemy Base
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationship to interactions
    interactions = relationship("Interaction", back_populates="user")

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"

class Video(Base):
    __tablename__ = "videos"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    category = Column(String, nullable=False)
    url = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationship to interactions
    interactions = relationship("Interaction", back_populates="video")

    def __repr__(self):
        return f"<Video(title='{self.title}', category='{self.category}')>"

class Interaction(Base):
    __tablename__ = "interactions"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    video_id = Column(Integer, ForeignKey("videos.id"), nullable=False)
    interaction_type = Column(String, nullable=False)  # e.g., view, like, rate, inspire
    rating = Column(Float, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Define relationships to User and Video
    user = relationship("User", back_populates="interactions")
    video = relationship("Video", back_populates="interactions")

    def __repr__(self):
        return (f"<Interaction(user_id={self.user_id}, video_id={self.video_id}, "
                f"type='{self.interaction_type}', rating={self.rating})>")
