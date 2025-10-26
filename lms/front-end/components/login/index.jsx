'use client'
import Logo from '../shared/logo'
import {Form,Button, Input,Divider} from 'antd'
import 'animate.css';
import Link from 'next/link'
import {Image} from 'next/image'
const {Item} = Form
const Login =()=>{

    const onFinish=(values)=>{
        console.log(values)
    }

    return(
        <div className='bg-gray-100 min-h-screen flex items-center justify-center'>
            <div className='animate__animated animate__zoomIn animate__faster bg-white rounded-lg p-8 md:w-4/12 w-11/12 flex flex-col gap-y-4'>
                <div className='flex items-center'>
                    <h1 className='font-semibold text-2xl'>Say Hi.</h1>
                    <Logo/>
                </div>

                {/* to get form value we will pass a function */}
                <Form 
                onFinish={onFinish}
                layout='vertical'
                >
                    <Item 
                    name="email"
                    label="Email:"
                    rules={[
                        {required:true, message:'This field is required'}
                    ]}
                    >
                        <Input placeholder="Email*" style={{borderRadius:0}} className='large' /> 
                    </Item>
                    <Item>
                        <Button
                        htmlType='submit'
                        style={{borderRadius:0}} 
                        className='w-full bg-indigo-900 text-white border-indigo-900 font-semibold  '
                        >Login</Button> 
                    </Item>
                </Form>

                <Divider orientation="center">
                    Or
                </Divider>
                
                <Button 
                      icon={<img src="/icons/google.png" alt="Google" width={32} height={32} />}
                      className='py-6 font-semibold'

                >
                    Continue with Google
                </Button>
                <Button 
                      icon={<img src="/icons/facebook.png" alt="Facebook" width={32} height={32} />}
                      className='py-6 font-semibold'
                >
                    Continue with Facebook
                </Button>
                <Divider/>
                <div className='flex gap-x-2 justify-center' >
                    Don't have an account?
                    <Link href="\register" className='text-indigo-900 font-semibold'>
                       Regester Now
                    </Link> 
                </div>
            </div>
        </div>
    )
}

export default Login