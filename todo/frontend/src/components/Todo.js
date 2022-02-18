import React from 'react';
import { MDBTable, MDBTableHead, MDBTableBody } from 'mdb-react-ui-kit';

const TodoItem = ({todo, users, projects, i}) => {
    return (
        <tr key={i}>
            <td>
                {projects.find(project => project.id == todo.project.toString()).name}
            </td>
            <td>
                {users.find(user => user.id == todo.owner.toString()).username}
            </td>
            <td>
                {todo.text}
            </td>
            <td>
                {String(todo.isActive)}
            </td>
        </tr>
    )
}

const TodoList = ({todos, users, projects}) => {
    return (
        <div className="container-fluid col-md-6 text-center marginTop58">
            <MDBTable hover>
                <MDBTableHead dark>
                    <tr>
                        <th scope="col">Проект</th>
                        <th scope="col">Автор</th>
                        <th scope="col">Текст</th>
                        <th scope="col">Активно</th>
                    </tr>
                </MDBTableHead>
                <MDBTableBody>
                    {todos.map((todo, i) => <TodoItem todo={todo} users={users} projects={projects} key={i} />)}
                </MDBTableBody>
            </MDBTable>
        </div>
    )
}

export default TodoList;