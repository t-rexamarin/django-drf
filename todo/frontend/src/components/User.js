import React from 'react';
import { MDBTable, MDBTableHead, MDBTableBody } from 'mdb-react-ui-kit';

const UserItem = ({user}) => {
    return (
        <tr>
            <td>
                {user.username}
            </td>
            <td>
                {user.email}
            </td>
            <td>
                {user.birthday_date}
            </td>
        </tr>
    )
}

const UserList = ({users}) => {
    return (
        <div className="container-fluid col-md-6 text-center" style={{marginTop: 58}}>
            <MDBTable hover>
                <MDBTableHead dark>
                    <tr>
                        <th scope="col">Юзернейм</th>
                        <th scope="col">Почта</th>
                        <th scope="col">Дата рождения</th>
                    </tr>
                </MDBTableHead>
                <MDBTableBody>
                    {users.map((user) => <UserItem user={user} />)}
                </MDBTableBody>
            </MDBTable>
        </div>
    )
}

export default UserList;