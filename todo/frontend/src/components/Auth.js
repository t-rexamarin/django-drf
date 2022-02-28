import React from 'react';
import {
  MDBInput,
  MDBCol,
  MDBRow,
  MDBCheckbox,
  MDBBtn
} from 'mdb-react-ui-kit';


class LoginForm extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            'login': '',
            'password': ''
        }
    }

    handleChange(event){
        this.setState({
            [event.target.name] : event.target.value
        });
        //console.log([event.target.name] + ' ' + event.target.value);
    }

    handleSubmit(event){
        this.props.get_token(this.state.login, this.state.password)
        event.preventDefault()
        // console.log(this.state.login + ' ' + this.state.password)
    }

    render(){
        return (
            <div className='loginBlock container-fluid col-md-6 text-center'>
                <form onSubmit={(event) => this.handleSubmit(event)}>
                    <MDBInput className='mb-4' type='login' name='login' label='Login'
                         onChange={(event) => this.handleChange(event)} />
                    <MDBInput className='mb-4' type='password' name='password' label='Password'
                        onChange={(event) => this.handleChange(event)} />

                    <MDBBtn type='submit' block>
                        Sign in
                    </MDBBtn>
                </form>
            </div>
        );
    }

}


export default LoginForm