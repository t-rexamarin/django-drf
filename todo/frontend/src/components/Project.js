import React from 'react';
import { MDBTable, MDBTableHead, MDBTableBody } from 'mdb-react-ui-kit';
import {Link} from 'react-router-dom';

const ProjectItem = ({project, users, i}) => {
    let users_arr = []
    let users_f = () => {
        project.users.map(userID => {
            let project_users = users.find(user => user.id == userID)

            if(project_users){
                users_arr.push(project_users.username)
            }
        })
        if(users_arr){
            return users_arr.join(', ')
        }
    }

    return (
        <tr key={i}>
            <td>
                <Link to={`project/${project.id}`}>{project.name}</Link>
            </td>
            <td>
                {project.link}
            </td>
            <td>
                {users_f()}
                {/* {project.users.map((userID) => {return users.find(user => user.id == userID).username}).join(', ')}*/}
            </td>
        </tr>
    )
}

const ProjectList = ({projects, users}) => {
    return (
        <div className="container-fluid col-md-6 text-center marginTopBottom58">
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
            <Link to='/projects/create'>Create Todo</Link>
        </div>
    )
}

export default ProjectList;