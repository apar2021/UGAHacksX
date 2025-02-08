// src/components/CollaboratorCard.js
import React from 'react';

const CollaboratorCard = ({ collaborator }) => {
  return (
    <div className="collaborator-card">
      <h3>{collaborator.name}</h3>
      <p><strong>Instrument:</strong> {collaborator.instrument}</p>
      <p><strong>Genre:</strong> {collaborator.genre}</p>
      <p><strong>Location:</strong> {collaborator.location}</p>
    </div>
  );
};

export default CollaboratorCard;
