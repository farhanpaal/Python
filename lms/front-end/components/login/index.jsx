'use client'
import Logo from '../shared/logo'
import {Form,Button, Input} from 'antd'
const {Item} = Form
const Login =()=>{
    return(
        <div className='bg-gray-100 min-h-screen flex items-center justify-center'>
            <div className='bg-white rounded-lg p-8 w-4/12 flex flex-col gap-y-4'>
                <div className='flex items-center'>
                    <h1 className='font-semibold text-2xl'>My login page</h1>
                    <Logo/>
                </div>
                <Form>
                    <Item >
                        <Input placeholder="Enter Name" style={{borderRadius:0}} className='large' /> 
                    </Item>
                    <Item>
                        <Button
                        style={{borderRadius:0}} 
                        className='w-full bg-indigo-900 text-white border-indigo-900 font-semibold  '
                        >Login</Button> 
                    </Item>
                </Form>
            </div>
        </div>
    )
}

export default Login