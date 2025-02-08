import React, { useState } from 'react';
import Header from './components/Header';
import PreferencesForm from './components/Preferences';
import BandMemberList from './components/BandMemberList';

const App = () => {
  const [preferences, setPreferences] = useState(null);
  const [collaborators, setCollaborators] = useState([]);

  // Sample collaborator data (this could come from an API)
  const sampleCollaborators = [
    { name: 'John Doe', instrument: 'Guitar', genre: 'Rock', location: 'New York' },
    { name: 'Jane Smith', instrument: 'Drums', genre: 'Metal', location: 'Los Angeles' },
    { name: 'Alice Johnson', instrument: 'Bass', genre: 'Jazz', location: 'Chicago' },
    { name: 'Mike Brown', instrument: 'Vocals', genre: 'Rock', location: 'New York' },
  ];

  // Handle form submission
  const handlePreferencesSubmit = (prefs) => {
    setPreferences(prefs);
    filterCollaborators(prefs);
  };

  // Filter collaborators based on preferences
  const filterCollaborators = (prefs) => {
    const filtered = sampleCollaborators.filter((collaborator) => {
      return (
        collaborator.instrument.toLowerCase().includes(prefs.instrument.toLowerCase()) &&
        collaborator.genre.toLowerCase().includes(prefs.genre.toLowerCase()) &&
        collaborator.location.toLowerCase().includes(prefs.location.toLowerCase())
      );
    });
    setCollaborators(filtered);
  };

  return (
    <div className="app">
      <Header />
      <PreferencesForm onSubmit={handlePreferencesSubmit} />
      <BandMemberList collaborators={collaborators} />
    </div>
  );
};

export default App;