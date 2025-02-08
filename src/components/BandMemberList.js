import React from 'react';
import CollaboratorCard from './CollaboratorCard';

const BandMemberList = ({ collaborators }) => {
  return (
    <div className="collaborator-list">
      {collaborators.length > 0 ? (
        collaborators.map((collaborator, index) => (
          <CollaboratorCard key={index} collaborator={collaborator} />
        ))
      ) : (
        <p>No collaborators found. Try adjusting your preferences.</p>
      )}
    </div>
  );
};

export default BandMemberList;
