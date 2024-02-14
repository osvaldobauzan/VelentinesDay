function addParticipant() {
    var participantInput = document.getElementById("participant-input");
    var participant = participantInput.value.trim();
    if (participant !== "") {
        fetch("/add_participant", {
            method: "POST",
            body: JSON.stringify({ participant: participant }),
            headers: {
                "Content-Type": "application/json"
            }
        })
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error("Error al agregar el participante.");
            }
        })
        .then(data => {
            alert(data.message);
            participantInput.value = "";
        })
        .catch(error => {
            alert(error.message);
        });
    } else {
        alert("Por favor, ingrese un nombre de participante.");
    }
}

function selectNext() {
    fetch("/select_next")
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error("Error al seleccionar el siguiente participante.");
        }
    })
    .then(data => {
        var selectedParticipantElement = document.getElementById("selected-participant");
        selectedParticipantElement.textContent = "El siguiente participante es: " + data.selected_participant;
    })
    .catch(error => {
        alert(error.message);
    });
}

function resetSelection() {
    fetch("/reset_selection")
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error("Error al reiniciar la selección.");
        }
    })
    .then(data => {
        alert(data.message);
        var selectedParticipantElement = document.getElementById("selected-participant");
        selectedParticipantElement.textContent = "";
    })
    .catch(error => {
        alert(error.message);
    });
}
