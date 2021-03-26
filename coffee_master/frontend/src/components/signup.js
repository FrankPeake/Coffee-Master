import React from 'react';
import './Signup.css';

class Signup extends React.Component{
    state = {
        username: '',
        password: '',
        first_name: '',
        last_name: '',
        email: '',
        city: '',
        st: ''
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
                <div className='signup-green'></div>
                <div className='login-form'>
                    <h1 className='login-heading'>Sign Up</h1>
                    <form onSubmit = {this.handleSubmit}>
                        <input type='text' name='username' placeholder="Username" required onChange={this.handleChange}/>
                        <input type='password' name='password' placeholder="Password" required onChange={this.handleChange}/>
                        <input type='text' name='first_name' placeholder="First Name" required onChange={this.handleChange}/>
                        <input type='text' name='last_name' placeholder="Last Name" required onChange={this.handleChange}/>
                        <input type='text' name='email' placeholder="Email Address" required onChange={this.handleChange}/>
                        <input type='text' name='city' placeholder="City" required onChange={this.handleChange}/>
                        <input type='text' name='st' placeholder="State" required onChange={this.handleChange}/>
                        <button onSubmit = {this.handleSubmit} className='login-btn'>Sign Up</button>
                    </form>
                </div>        
            </div>
        )
    }
}

export default Signup;
