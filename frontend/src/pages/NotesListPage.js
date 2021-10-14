import React, { useState, useEffect } from 'react'
import ListItem from '../components/ListItem.js'
import AddButton from '../components/AddButton.js'

const NotesListPage = () => {

    let [notes, setNotes] = useState([])

    useEffect(() => {
        getNotes()
    }, []);

    let getNotes = async () => {
        // This causes a CORS error (since backend is on 8000 and frontend is on 3000)
        // We can solve this with django cors headers
        let response = await fetch('/api/notes/')
        let data = await response.json()
        setNotes(data)
        console.log(data)
    }

    return (
        <div className = "notes">
            <div className = "notes-header">
                <h2 className = "notes-title"> &#9782; Notes </h2>
                <p className = "notes-count"> {notes.length} </p>
            </div>
            <div className = "notes-list">
                {notes.map((note, index) => (
                    <ListItem key = {index} note={note} />
                ))}
            </div>
            <AddButton />
        </div>
    )
}

export default NotesListPage

