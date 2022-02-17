import React from 'react';
import axios from 'axios';
import logo from './logo.svg';
import './App.css';
import UserList from './components/User';
import Menu from './components/Menu';
import Footer from './components/Footer';
import ProjectList from './components/Project';
import TodoList from './components/Todo';

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'todos': []
        };
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users/viewsets/base/').then(response => {
            const users = response.data;

            this.setState({
                'users': users
            });
        }).catch(error => console.log(error));

        axios.get('http://127.0.0.1:8000/api/projects/viewsets/project/').then(response => {
            const projects = response.data;

            this.setState({
                'projects': projects
            });
        }).catch(error => console.log(error));

        axios.get('http://127.0.0.1:8000/api/projects/viewsets/todo/').then(response => {
            const todos = response.data;

            this.setState({
                'todos': todos
            });
        }).catch(error => console.log(error));
    }

    render () {
        return (
            <div>
                <Menu />
                <UserList users={this.state.users} />
                <ProjectList projects={this.state.projects} />
                <TodoList todos={this.state.todos} />
                <Footer />
            </div>
        );
    }
}

export default App;