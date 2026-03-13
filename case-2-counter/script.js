const result = document.getElementById("result");
const plusBtn = document.getElementById("plusBtn");
const minusBtn = document.getElementById("minusBtn");
const message = document.getElementById("message");

let count = 0;

function updateInterface() {
    result.textContent = count;

    if (count > 0) {
        result.style.background = "yellow";
    } else if (count < 0) {
        result.style.background = "lightgreen";
    } else {
        result.style.background = "red";
    }

    plusBtn.disabled = count === 10;
    minusBtn.disabled = count === -10;

    if (count === 10 || count === -10) {
        message.textContent = "Вы достигли экстремального значения";
    } else {
        message.textContent = "";
    }
}

plusBtn.addEventListener("click", function () {
    if (count < 10) {
        count++;
        updateInterface();
    }
});

minusBtn.addEventListener("click", function () {
    if (count > -10) {
        count--;
        updateInterface();
    }
});

updateInterface();