import React from 'react';
import { MDBTable, MDBTableHead, MDBTableBody } from 'mdb-react-ui-kit';
import {Link, useParams} from 'react-router-dom';

const GetOneProjectItem = ({project, users, i}) => {
    return (
        <tr key={i}>
            <td>
                {project.name}
            </td>
            <td>
                {project.link}
            </td>
            <td>

                {/*{project.users.map((user) => user + ', ')}*/}
                {project.users.map((userID) => {return users.find(user => user.id == userID).username}).join(', ')}
                {/*{console.log(users.find(user => user.id == 198).username)}*/}
            </td>
        </tr>
    )

}

const GetOneProject = ({projects, users}) => {
    let {project_id} = useParams();
    let filtered_project_id = projects.filter((project) => project.id == project_id);

    return (
        <div className="container-fluid col-md-6 text-center marginTop58">
            <MDBTable hover>
                <MDBTableHead dark>
                    <tr>
                        <th scope="col">Название проекта</th>
                        <th scope="col">Ссылка на проект</th>
                        <th scope="col">Участники</th>
                    </tr>
                </MDBTableHead>
                <MDBTableBody>
                    {filtered_project_id.map((project, i) => <GetOneProjectItem project={project} users={users} key={i} />)}
                </MDBTableBody>
            </MDBTable>
        </div>
    )
}

export default GetOneProject;