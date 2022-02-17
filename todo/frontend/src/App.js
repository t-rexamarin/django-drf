import React from 'react';
import axios from 'axios';
import logo from './logo.svg';
import './App.css';
import UserList from './components/User';
import Menu from './components/Menu';
import Footer from './components/Footer';
import ProjectList from './components/Project';
import TodoList from './components/Todo';
import {HashRouter, Route} from 'react-router-dom';

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'todos': [],
            'menuLinks': [
                {'name': 'Users', 'href': '/'},
                {'name': 'Projects', 'href': '/projects'},
                {'name': 'Todos', 'href': '/todos'}
            ]
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
            <div className="App">
                <HashRouter>
                    <Menu menuLinks={this.state.menuLinks} />
                    <Route exact path='/' component={() => <UserList users={this.state.users} />} />
                    <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects} />} />
                    <Route exact path='/todos' component={() => <TodoList todos={this.state.todos} />} />
                    <Footer />
                </HashRouter>
            </div>
        );
    }
}

export default App;