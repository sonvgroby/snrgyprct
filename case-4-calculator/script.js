const num1 = document.getElementById("num1");
const num2 = document.getElementById("num2");
const result = document.getElementById("result");

document.getElementById("sumBtn").addEventListener("click", function () {
    calculate("+");
});

document.getElementById("subBtn").addEventListener("click", function () {
    calculate("-");
});

document.getElementById("mulBtn").addEventListener("click", function () {
    calculate("*");
});

document.getElementById("divBtn").addEventListener("click", function () {
    calculate("/");
});

function calculate(operation) {
    const value1 = num1.value.trim();
    const value2 = num2.value.trim();

    if (value1 === "" || value2 === "" || isNaN(value1) || isNaN(value2)) {
        result.textContent = "Ошибка: введите числа";
        return;
    }

    const a = Number(value1);
    const b = Number(value2);
    let answer;

    if (operation === "+") {
        answer = a + b;
    } else if (operation === "-") {
        answer = a - b;
    } else if (operation === "*") {
        answer = a * b;
    } else if (operation === "/") {
        if (b === 0) {
            result.textContent = "Ошибка: деление на ноль";
            return;
        }
        answer = a / b;
    }

    result.textContent = `Результат: ${answer}`;
}