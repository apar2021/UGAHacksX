import React, { useState } from 'react';

const PreferencesForm = ({ onSubmit }) => {
  const [preferences, setPreferences] = useState({
    instrument: '',
    genre: '',
    location: '',
  });

  const handleChange = (e) => {
    setPreferences({ ...preferences, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(preferences);
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Instrument</label>
        <input
          type="text"
          name="instrument"
          value={preferences.instrument}
          onChange={handleChange}
          placeholder="e.g. Guitar, Drums"
        />
      </div>
      <div>
        <label>Preferred Genre</label>
        <input
          type="text"
          name="genre"
          value={preferences.genre}
          onChange={handleChange}
          placeholder="e.g. Rock, Metal"
        />
      </div>
      <div>
        <label>Location</label>
        <input
          type="text"
          name="location"
          value={preferences.location}
          onChange={handleChange}
          placeholder="e.g. New York, LA"
        />
      </div>
      <button type="submit">Find Collaborators</button>
    </form>
  );
};

export default PreferencesForm;