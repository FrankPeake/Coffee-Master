import React from 'react';
import './Login.css';

class Login extends React.Component{
    state = {
        username: '',
        password: ''
    }

    handleChange = (e) => {
        const {name,value} = e.target
        this.setState({[name]:value})
    }

    handleSubmit = (e) => {
        e.preventDefault()
    }


    render(){
        return(
            <div className='login-container'>
                <div className='logo-wall'></div>
                <div className='login-form'>
                    <h1 className='login-heading'>Sign In</h1>
                    <form onSubmit = {this.handleSubmit}>
                        <input type='text' name='username' placeholder="Username" required onChange={this.handleChange}/>
                        <input type='password' name='password' placeholder="Password" required onChange={this.handleChange}/>
                        <button onSubmit = {this.handleSubmit} className='login-btn'>Login</button>
                        <h3 className='not_a_member'>Not a Member? Sign up <a href='/signup'>Here</a></h3>
                    </form>
                </div>        
            </div>
        )
    }
}

export default Login;
