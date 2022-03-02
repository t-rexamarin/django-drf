import React from 'react';
import axios from 'axios';
import logo from './logo.svg';
import './App.css';
import UserList from './components/User';
import Menu from './components/Menu';
import Footer from './components/Footer';
import ProjectList from './components/Project';
import GetOneProject from './components/GetOneProject';
import TodoList from './components/Todo';
import LoginForm from './components/Auth';
import Cookies from 'universal-cookie';
import {HashRouter, Route, Switch, Redirect} from 'react-router-dom';


const DOMAIN = 'http://127.0.0.1:8000/'
const get_url = (url) => `${DOMAIN}${url}`


const NotFound404 = ({location}) => {
    return (
        <div className="marginTop58">
            <h2>Страница  по адресу "{location.pathname}" не найдена</h2>
        </div>
    )
}


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
                {'name': 'Todos', 'href': '/todos'},
                //{'name': 'Login', 'href': '/login'},
            ],
            'token': '',
        };
    }

//    logout(){
//        this.set_token('')
//        console.log('no token')
//        this.state.menuLinks[3] = {'name': 'Login', 'href': '/login'}
//    }
    handleLogout(event){
        event.preventDefault()
        console.log('no token')
        this.set_token('')
        this.state.menuLinks[3] = {'name': 'Login', 'href': '/login'}
    }

    load_data(){
        const headers = this.get_headers()

        axios.get(get_url('api/users/viewsets/base/'), {headers}).then(response => {
            const users = response.data;

            this.setState({
                'users': users
            });
        }).catch(error => console.log(error));

        axios.get(get_url('api/projects/viewsets/project/'), {headers}).then(response => {
            const projects = response.data;

            this.setState({
                'projects': projects
            });
        }).catch(error => console.log(error));

        axios.get(get_url('api/projects/viewsets/todo/'), {headers}).then(response => {
            const todos = response.data;

            this.setState({
                'todos': todos
            });
        }).catch(error => console.log(error));

//        this.state.menuLinks[3] = {'name': 'Logout', 'href': '/'}
    }

    is_auth(){
        console.log(!!this.state.token)
        return !!this.state.token
    }

    get_token_from_cookies(){
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token}, () => this.load_data())
    }

    set_token(token){
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token}, () => this.load_data())
//        localStorage.setItem('token', token)
//        let token_ = localStorage.getItem('token')
//        document.cookie = `token=${token}`
    }

    get_token(username, password){
        axios.post(get_url('api-token-auth/'), {
            username: username,
            password: password
        }).then(response => {
            //console.log(response.data['token'])
            this.set_token(response.data['token'])
        }).catch(error => console.log(error));
        // console.log('APP ' + username + ' ' + password)
    }

    get_headers(){
        let headers = {
            'Content-Type':'application/json'
        }

        if(this.is_auth()){
            headers['Authorization'] = `Token ${this.state.token}`
        }

        return headers
    }

    componentDidMount() {
        this.get_token_from_cookies()
    }

    render () {
        return (
            <div className="App">
                <HashRouter>
                    <Menu menuLinks={this.state.menuLinks} is_auth={this.is_auth()} />

                    <Switch>
                        <Route exact path='/' component={() => <UserList users={this.state.users} />} />
                        <Route exact path='/projects' component={() =>
                            <ProjectList projects={this.state.projects} users={this.state.users}/>} />
                        <Route exact path='/todos' component={() =>
                            <TodoList todos={this.state.todos} users={this.state.users}
                            projects={this.state.projects} />} />
                        <Route path="/project/:project_id">
                            <GetOneProject projects={this.state.projects} users={this.state.users} />
                        </Route>
                        <Route exact path='/login'
                            component={() => <LoginForm
                                get_token={(username, password) => this.get_token(username, password)} />} />
                        <Redirect from='/users' to='/' />
                        <Route component={NotFound404} />
                    </Switch>
                    <Footer />
                </HashRouter>
            </div>
        );
    }
}

export default App;