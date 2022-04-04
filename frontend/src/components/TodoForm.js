import React from 'react';
import { MDBInput, MDBBtn } from 'mdb-react-ui-kit';

class TodoForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {owner: 0, project: 0, text: ''}
    }

    handleChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        })
    }

    handleEmptyRows() {
        let error = 0
        if(!this.state.owner) {
            alert('Select todo owner.')
            error = 1
        }

        if(!this.state.project) {
            alert('Select todo project.')
            error = 1
        }

        if(!this.state.text) {
            alert('Fill todo text.')
            error = 1
        }

        return error
    }

    handleSubmit(event) {
        event.preventDefault()

        if(this.handleEmptyRows()){
            return;
        }

        this.props.createTodo(this.state.owner, this.state.project, this.state.text)
//        console.log(this.state.owner)
//        console.log(this.state.project)
//        console.log(this.state.text)
    }

//    handleProjectChange(event) {
//        if(!event.target.selectedOptions) {
//            this.setState({
//                'project': []
//            })
//            return;
//        }
//
//        let projects = []
//        for (let i = 0; i < event.target.selectedOptions.length; i++) {
//            projects.push(event.target.selectedOptions.item(i).value)
//        }
//        this.setState({
//            'project': projects
//        })
//    }

    render() {
        return (
            <div className='marginTopBottom58 container-fluid col-md-6 text-center'>
                <p className='pt-2 mb-2'>Todo creation form</p>
                <form className='form-inline' onSubmit={(event) => this.handleSubmit(event)}>
                    {/* <MDBInput className='mb-4' type='text' name='project' label='Project'
                         onChange={(event) => this.handleChange(event)} />*/}
                    {/* <MDBInput className='mb-4' type='text' name='owner' label='Owner'
                        onChange={(event) => this.handleChange(event)} />*/}
                    <div className='form-group'>
                        <label for='project' class="col-sm-2 control-label d-flex justify-content-start">Project</label>
                        <select className='form-control mb-1' name='project' id='project' onChange={(event) => this.handleChange(event)}>
                            <option value='' selected disabled>Select todo project</option>
                            {this.props.projects.map((item, index) => <option value={item.id}>{item.name}</option>)}
                        </select>
                        <label for='owner' class="col-sm-2 control-label d-flex justify-content-start">Owner</label>
                        <select className='form-control mb-4' name='owner' id='owner' onChange={(event) => this.handleChange(event)}>
                            <option value='' selected disabled>Select todo owner</option>
                            {this.props.users.map((item, index) => <option value={item.id}>{item.username}</option>)}
                        </select>
                    </div>
                    <MDBInput className='mb-4' type='text' name='text' label='Text'
                        onChange={(event) => this.handleChange(event)} />

                    <MDBBtn type='submit' block>
                        Send
                    </MDBBtn>
                </form>
            </div>
        )
    }
}

export default TodoForm;