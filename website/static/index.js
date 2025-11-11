function deleteNote(noteId) {
    fetch('/delete-note', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ noteId: noteId })
    })
    .then(res => res.json())
    .then(data => {
        if (data.success) {
            window.location.href = "/";
        } else {
            alert("Failed to delete note");
        }
    });
}
/*
function deleteNote(noteId){
    fetch('/delete-note', {
        method: 'POST',
        body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
        window.location.href = "/";
    });
}
*/