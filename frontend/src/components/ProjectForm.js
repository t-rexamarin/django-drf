import React from 'react';
import { MDBInput, MDBBtn } from 'mdb-react-ui-kit';

class ProjectForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {name: '', link: '', users: []}
    }

    handleChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        })
    }

    handleEmptyRows() {
        let error = 0
        if(!this.state.name) {
            alert('Write project name.')
            error = 1
        }

        if(!this.state.link) {
            alert('Write project link.')
            error = 1
        }

        if(!this.state.users) {
            alert('Choose project users.')
            error = 1
        }

        return error
    }

    handleSubmit(event) {
        event.preventDefault()

        if(this.handleEmptyRows()){
            return;
        }

        this.props.createProject(this.state.name, this.state.link, this.state.users)
//        console.log(this.state.owner)
//        console.log(this.state.project)
//        console.log(this.state.text)
    }

    handleUsersChange(event) {
        if(!event.target.selectedOptions) {
            this.setState({
                'users': []
            })
            return;
        }

        let users = []
        for (let i = 0; i < event.target.selectedOptions.length; i++) {
            users.push(event.target.selectedOptions.item(i).value)
        }
        this.setState({
            'users': users
        })
    }

    render() {
        return (
            <div className='marginTopBottom58 container-fluid col-md-6 text-center'>
                <p className='pt-2 mb-2'>Project creation form</p>
                <form className='form-inline' onSubmit={(event) => this.handleSubmit(event)}>
                    <MDBInput className='mb-4' type='text' name='name' label='Project name'
                         onChange={(event) => this.handleChange(event)} />
                    <MDBInput className='mb-4' type='text' name='link' label='Project link'
                        onChange={(event) => this.handleChange(event)} />
                    <div className='form-group'>
                        <label for='users' class="col-sm-2 control-label d-flex justify-content-start">Users</label>
                        <select className='form-control mb-4' name='users' id='users' multiple onChange={(event) => this.handleUsersChange(event)}>
                            {this.props.users.map((item, index) => <option value={item.id}>{item.username}</option>)}
                        </select>
                    </div>

                    <MDBBtn type='submit' block>
                        Send
                    </MDBBtn>
                </form>
            </div>
        )
    }
}

export default ProjectForm;