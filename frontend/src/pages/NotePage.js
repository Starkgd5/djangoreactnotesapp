import React, { useState, useEffect, useCallback } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { ReactComponent as ArrowLeft } from '../assets/arrow-left.svg';

const NotePage = () => {
  const { id: noteId } = useParams();
  const navigate = useNavigate();
  const [note, setNote] = useState({ body: '' });

  const fetchNote = useCallback(async () => {
    try {
      const response = await fetch(`/api/notes/${noteId}/`);
      const data = await response.json();
      setNote(data);
    } catch (error) {
      console.error('Error fetching note:', error);
    }
  }, [noteId]);

  useEffect(() => {
    if (noteId !== 'new') {
      fetchNote();
    }
  }, [fetchNote, noteId]);

  const saveNote = async (method, url) => {
    try {
      await fetch(url, {
        method,
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(note),
      });
    } catch (error) {
      console.error(`Error ${method === 'PUT' ? 'updating' : 'creating'} note:`, error);
    }
  };

  const deleteNote = async () => {
    try {
      await fetch(`/api/notes/${noteId}/`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
        },
      });
      navigate('/');
    } catch (error) {
      console.error('Error deleting note:', error);
    }
  };

  const handleSubmit = async () => {
    if (noteId !== 'new' && note.body === '') {
      await deleteNote();
    } else if (noteId !== 'new') {
      await saveNote('PUT', `/api/notes/${noteId}/`);
    } else if (noteId === 'new' && note.body !== '') {
      await saveNote('POST', `/api/notes/`);
    }
    navigate('/');
  };

  const handleChange = (e) => {
    setNote(prevNote => ({ ...prevNote, body: e.target.value }));
  };

  return (
    <div className="note">
      <div className="note-header">
        <h3>
          <ArrowLeft onClick={handleSubmit} />
        </h3>
        {noteId !== 'new' ? (
          <button onClick={deleteNote}>Delete</button>
        ) : (
          <button onClick={handleSubmit}>Done</button>
        )}
      </div>
      <textarea onChange={handleChange} value={note.body}></textarea>
    </div>
  );
};

export default NotePage;
