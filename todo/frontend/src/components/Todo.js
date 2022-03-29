import React from 'react';
import { Link } from 'react-router-dom';
import { MDBTable, MDBTableHead, MDBTableBody, MDBBtn } from 'mdb-react-ui-kit';

const TodoItem = ({todo, users, projects, i, deleteTodo}) => {
    let project = () => {
        let project_name = projects.find(project => project.id == todo.project)
        if(project_name){
            return project_name.name
        }
    }

    let user = () => {
                        let proj_owner = users.find(user_obj => user_obj.id == todo.owner)
                        if(proj_owner){
                            return proj_owner.username
                        }
                    }

    return (
        <tr key={i}>
            <td>
               {/* {projects.find(project => project.id == todo.project.toString()).name}*/}
               {/* {projects.find(project => project.id == todo.project.toString())}*/}
               {/* {todo.project}*/}
               {project()}
            </td>
            <td>
                {user()}
                {/* {users.map((userID) => {
                    let user = users.find(userID => userID.id == todo.owner)

                    if(user){
                        return user
                    }
                }).username}*/}
                {/* {todo.owner}*/}
            </td>
            <td>
                {todo.text}
            </td>
            <td>
                {String(todo.isActive)}
            </td>
            <td>
                <MDBBtn color='warning' onClick={() => deleteTodo(todo.id)}>Delete</MDBBtn>
            </td>
        </tr>
    )
}

const TodoList = ({todos, users, projects, deleteTodo}) => {
    return (
        <div className="container-fluid col-md-6 text-center marginTopBottom58">
            <MDBTable hover>
                <MDBTableHead dark>
                    <tr>
                        <th scope="col">Проект</th>
                        <th scope="col">Автор</th>
                        <th scope="col">Текст</th>
                        <th scope="col">Активно</th>
                        <th scope="col"></th>
                    </tr>
                </MDBTableHead>
                <MDBTableBody>
                    {todos.map((todo, i) => <TodoItem todo={todo} users={users} projects={projects} key={i}
                    deleteTodo={deleteTodo} />)}
                </MDBTableBody>
            </MDBTable>
            <Link to='/todos/create'>Create Todo</Link>
        </div>
    )
}

export default TodoList;