
// select the todo-form
const todoForm = document.querySelector('.todo-form');
// select the input box
const todoInput = document.querySelector('.todo-input');
// select the <ul> with class="todo-items"
const todoItemsList = document.querySelector('.todo-items');
// array which stores tasks
let todos = [];
// add an eventListener on form, and listen for submit event
todoForm.addEventListener('submit', function(event) {
    addTodo(todoInput.value); // call addTodo function with input box current value
});
// function to add todo
function addTodo(item) {
    if (item !== '') {
        // make a todo object
        const todo = {
            id: Date.now(),
            name: item,
            completed: false
        };
        todos.push(todo);
        addToLocalStorage(todos); //store it in local storage
        todoInput.value = '';
    }
}
// function to render given todos to screen
function renderTodos(todos) {

    todoItemsList.innerHTML = '';

    todos.forEach(function(item) {

        const checked = item.completed ? 'checked': null;

        const li = document.createElement('li');

        li.setAttribute('class', 'item');

        li.setAttribute('data-key', item.id);
        if (item.completed === true) {
            li.classList.add('checked');
        }
        li.innerHTML = `
      <input type="checkbox" class="checkbox" ${checked}>
      ${item.name}
      <button class="delete-button">X</button>
    `;

        todoItemsList.append(li);
    });
}

function addToLocalStorage(todos) {
    // convert the array to string then store it.
    localStorage.setItem('todos', JSON.stringify(todos));
    renderTodos(todos);
}
function getFromLocalStorage() {
    const reference = localStorage.getItem('todos');
    if (reference) {
        todos = JSON.parse(reference);
        renderTodos(todos);
    }
}

function toggle(id) {
    todos.forEach(function(item) {
        if (item.id == id) {
            item.completed = !item.completed;
        }
    });
    addToLocalStorage(todos);
}
function deleteTodo(id) {
    // filters out the list with the id and updates the todos array
    todos = todos.filter(function(item) {
        return item.id != id;
    });
    addToLocalStorage(todos);
}

getFromLocalStorage();

todoItemsList.addEventListener('click', function(event) {
    if (event.target.type === 'checkbox') {
        toggle(event.target.parentElement.getAttribute('data-key'));
    }
    if (event.target.classList.contains('delete-button')) {
        deleteTodo(event.target.parentElement.getAttribute('data-key'));
    }
});