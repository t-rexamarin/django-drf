import React from 'react';
import { MDBTable, MDBTableHead, MDBTableBody } from 'mdb-react-ui-kit';
import {Link} from 'react-router-dom';

const ProjectItem = ({project, users, i}) => {
    return (
        <tr key={i}>
            <td>
                <Link to={`project/${project.id}`}>{project.name}</Link>
            </td>
            <td>
                {project.link}
            </td>
            <td>
                {project.users.map((userID) => {return users.find(user => user.id == userID).username}).join(', ')}
            </td>
        </tr>
    )
}

const ProjectList = ({projects, users}) => {
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
                    {projects.map((project, i) => <ProjectItem project={project} users={users} key={i} />)}
                </MDBTableBody>
            </MDBTable>
        </div>
    )
}

export default ProjectList;