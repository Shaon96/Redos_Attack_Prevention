import logo from './logo.svg';
import React from "react";
import "./App.css";
import { Button, Card, Form } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  const [todos, setTodos] = React.useState([
    {
      text: "This is a sample todo",
      isDone: false
    }
  ]);

  const addTodo = text => {
    // use humanize ms here
    var ms = require('humanize-ms');
    // var splitted_words = text.split(' ')
    // var transformed_words = []
    // var words = []
    // for(var i=0; i < splitted_words.length; i++){
    //   if(i < (splitted_words.length - 1)){
    //     if(splitted_words[i+1] == 'minutes' || splitted_words[i+1] == 'hours' || splitted_words[i+1] == 'secs' || splitted_words[i+1] == 'm' || splitted_words[i+1] == 'h' || splitted_words[i+1] =='d'){
    //       words.push(splitted_words[i] + ' '+ splitted_words[i+1])
    //       i=i+1
    //     }
    //   }
    // }
    // for(var word in words) {
    //   console.log(word)
    //   var transformed_word = ms(word)
    //   if(transformed_word != undefined){
    //     var convert_to_days = (transformed_word/(1000*60*60*24))
    //     if(convert_to_days > 0) {
    //       transformed_words.push("["+ convert_to_days + " days]")
    //     }
    //     else
    //       transformed_words.push("["+word+"]")
    //   }
    //   else
    //     transformed_words.push(word)
    // }
    // var transformed_text = ""
    // for(var word in transformed_words){
    //   console.log("===" + word)
    //   transformed_text += word + " "
    // } 
    // // var transformed_text = transformed_words.join(' ')
    // console.log(transformed_text)
    // console.log(text)
    var transformed_text = ms(text) // 1000
    console.log(transformed_text)
    // ms(1000) // 1000
    const newTodos = [...todos, { text }];
    setTodos(newTodos);
  };

  const markTodo = index => {
    const newTodos = [...todos];
    newTodos[index].isDone = true;
    setTodos(newTodos);
  };


  const removeTodo = index => {
    const newTodos = [...todos];
    newTodos.splice(index, 1);
    setTodos(newTodos);
  };

  return (
    <div className="App">
      <div className="app">
      <div className="container">
        <h1 className="text-center mb-4">Todo List</h1>
        <FormTodo addTodo={addTodo} />
        <div>
          {todos.map((todo, index) => (
            <Card>
              <Card.Body>
                <Todo
                key={index}
                index={index}
                todo={todo}
                markTodo={markTodo}
                removeTodo={removeTodo}
                />
              </Card.Body>
            </Card>
          ))}
        </div>
      </div>
    </div>
    </div>
  );
}

function Todo({ todo, index, markTodo, removeTodo }) {
  return (
    <div
      className="todo"
      
    >
      <span style={{ textDecoration: todo.isDone ? "line-through" : "" }}>{todo.text}</span>
      <div>
        <Button variant="outline-success" onClick={() => markTodo(index)}>✓</Button>{' '}
        <Button variant="outline-danger" onClick={() => removeTodo(index)}>✕</Button>
      </div>
    </div>
  );
}

function FormTodo({ addTodo }) {
  const [value, setValue] = React.useState("");

  const handleSubmit = e => {
    e.preventDefault();
    if (!value) return;
    addTodo(value);
    setValue("");
  };

  return (
    <Form onSubmit={handleSubmit}> 
    <Form.Group>
      <Form.Label><b>Add Todo</b></Form.Label>
      <Form.Control type="text" className="input" value={value} onChange={e => setValue(e.target.value)} placeholder="Add new todo" />
    </Form.Group>
    <Button variant="primary mb-3" type="submit">
      Submit
    </Button>
  </Form>
  );
}


export default App;
