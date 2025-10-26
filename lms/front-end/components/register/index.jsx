'use client'
import Logo from '../shared/logo'
import Country from '../../public/json/country.json'
import { Form, Button, Input, Divider, Select } from 'antd'
import 'animate.css';
import Link from 'next/link'
import Image from 'next/image'
const { Item } = Form
const { Option } = Select

const Register = () => {
    const onFinish=(values)=>{
        values.mobile=(values.prefix+values.mobile)
        console.log(values)
    }

    const prefixSelector = (
        <Item 
        name="prefix" 
        noStyle
        rules={[{required:true, message:'Enter country code'}]}
        
        >
            <Select style={{ width: 120 }}
                placeholder="+00"
                
            >
                {
                    Country.map((item, index) => (
                        <Option key={index} value={item.dial_code}>
                            {item.dial_code} {item.code}
                        </Option>
                    ))
                }
            </Select>
        </Item>
    );



    return (

        <div className='flex min-h-screen md:flex-row flex-col w-screen animate__animated animate__fadeIn'>

            <div className='flex items-center justify-center flex-col gap-y-8 md:w-6/12'>
                {/* Mobile: 20, Desktop: 50 */}
                <div className="block sm:hidden">
                    <Logo size={30} />
                </div>
                <div className="hidden sm:block">
                    <Logo size={50} />
                </div>
                <Image
                    src="/images/register.png"
                    width={500}
                    height={500}
                    alt="register img"
                    className="w-40 sm:w-60 md:w-80 lg:w-[500px] h-auto"
                />
            </div>
            <div className='bg-gray-200 md:w-6/12 w-full flex justify-center items-center'>
                <div className='flex flex-col justify-center items-center '>
                    <h1 className='font-semibold py-5 text-xl'>Start your journey</h1>
                    <Form
                        onFinish={onFinish}
                        className='md:w-full '
                        layout='vertical'

                    >
                        <Item
                            name="fullname"

                            rules={[
                                { required: true, message: 'This field is required' }
                            ]}
                        >
                            <Input placeholder="Full name" style={{ borderRadius: 0 }} className='large' />
                        </Item>

                        <Item
                            name="email"

                            rules={[
                                { required: true, message: 'This field is required' }
                            ]}
                        >
                            <Input placeholder="Email*" style={{ borderRadius: 0 }} className='large' />
                        </Item>

                        <Item
                            name="password"

                            rules={[
                                { required: true, message: 'This field is required' }
                            ]}
                        >
                            <Input type="password" placeholder="*********" style={{ borderRadius: 0 }} className='large' />
                        </Item>
                        <Item
                            name="mobile"
                            rules={[{
                                 required: true, message: 'Please input your phone number!'
                                 }]}
                        >
                            <Input addonBefore={prefixSelector} style={{ width: '100%' }} placeholder="mobile" />
                        </Item>
                        <Item>
                            <Button
                                htmlType='submit'
                                style={{ borderRadius: 0 }}
                                className='w-full bg-indigo-900 text-white border-indigo-900 font-semibold  '
                            >Login</Button>
                        </Item>
                    </Form>
                    <div className='flex gap-x-2 justify-center py-10' >
                        Have an account?
                        <Link href="\login" className='text-indigo-900 font-semibold'>
                            Login Now
                        </Link>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Register


