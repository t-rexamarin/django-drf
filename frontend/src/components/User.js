import React from 'react';
import { MDBTable, MDBTableHead, MDBTableBody } from 'mdb-react-ui-kit';

const UserItem = ({user, i}) => {
    return (
        <tr key={i}>
            <td>
                {user.username}
            </td>
            <td>
                {user.email}
            </td>
            <td>
                {user.birthdayDate}
            </td>
        </tr>
    )
}

const UserList = ({users}) => {
    return (
        <div className="container-fluid col-md-6 text-center marginTopBottom58">
            <MDBTable hover>
                <MDBTableHead dark>
                    <tr>
                        <th scope="col">Юзернейм</th>
                        <th scope="col">Почта</th>
                        <th scope="col">Дата рождения</th>
                    </tr>
                </MDBTableHead>
                <MDBTableBody>
                    {users.map((user, i) => <UserItem user={user} key={i} />)}
                </MDBTableBody>
            </MDBTable>
        </div>
    )
}

export default UserList;