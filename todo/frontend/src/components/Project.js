import React from 'react';
import { MDBTable, MDBTableHead, MDBTableBody } from 'mdb-react-ui-kit';

const ProjectItem = ({project, i}) => {
    return (
        <tr key={i}>
            <td>
                {project.name}
            </td>
            <td>
                {project.link}
            </td>
            <td>
                {/* править костыль */}
                {project.users.map((user) => user + ', ')}
            </td>
        </tr>
    )
}

const ProjectList = ({projects}) => {
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
                    {projects.map((project, i) => <ProjectItem project={project} key={i} />)}
                </MDBTableBody>
            </MDBTable>
        </div>
    )
}

export default ProjectList;