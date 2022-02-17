import React from 'react';
import { MDBTable, MDBTableHead, MDBTableBody } from 'mdb-react-ui-kit';

const TodoItem = ({todo, i}) => {
    return (
        <tr key={i}>
            <td>
                {todo.project}
            </td>
            <td>
                {todo.owner}
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

const TodoList = ({todos}) => {
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
                    {todos.map((todo, i) => <TodoItem todo={todo} key={i} />)}
                </MDBTableBody>
            </MDBTable>
        </div>
    )
}

export default TodoList;