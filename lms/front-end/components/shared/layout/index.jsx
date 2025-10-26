'use client'

import { Layout, Button, Menu, Spin } from 'antd'
import Logo from '../logo/index'
import { useState, useEffect } from 'react'
import Link from 'next/link'
const { Sider, Content, Header } = Layout
const { Item } = Menu
import { DashboardOutlined, VideoCameraOutlined, PicCenterOutlined } from '@ant-design/icons'



// In antdesign there is already Layout defined, so we wrote here LayoutEl

const LayoutEl = ({ children, title=null, subtitle=null, toolbar=null }) => {  //we destructure children, it will hold the code we wrote in between layout
    const [open, setOpen] = useState(true);
    const [loader, setLoader] = useState(true);
    useEffect(() => {
        let releaseTimer = setTimeout(() => {
            setLoader(false), 3000
        })
        return () => {
            clearTimeout(releaseTimer)
        }

    })


    // array of objects menus
    const menus = [
        {
            label: 'Dashboard',
            href: '/admin',
            icon: <DashboardOutlined />
        },
        {
            label: 'Courses',
            href: '/admin/courses',
            icon: <VideoCameraOutlined />
        },
    ]

    // if(loader) 
    //     return(
    //         <div className='flex min-h-screen items-center justify-center'> 

    //         <Spin size="large"/>
    //         </div>
    //     ) 

    return (
        <Layout>

            <Sider className='min-h-screen' trigger={null} collapsible collapsed={close}>
                <div>
                    <Logo
                        size={32}
                        color="white"
                        padding='20px'
                    />
                </div>
                <Menu theme="dark">
                    {
                        menus.map((item, index) => (
                            <Item key={index} icon={item.icon}>
                                <Link href={item.href}>{item.label}</Link>
                            </Item>
                        ))
                    }
                </Menu>
            </Sider>


            <Layout>
                <Header className="!bg-white h-20 flex px-6 justify-between items-center">
                    <div className="flex items-center gap-x-6">
                        <Button
                            onClick={() => setOpen(!open)}
                            icon={<PicCenterOutlined />}
                            style={{
                                width: 40,
                                height: 40
                            }}
                            className="flex justify-center items-center"
                        />
                        <div>
                            {
                                title &&
                                <h1 className="text-lg font-semibold">{title}</h1>
                                // means is there title inside title, then display h1 tag
                            }
                            {
                                subtitle &&
                                <p className='text-sm text-zinc-500'>{subtitle}</p>
                            }
                        </div>
                    </div>
                    <div className="flex gap-x-4 items-center">
                        {toolbar}
                    </div>
                </Header>

                <Content className='p-8'>
                    {children}
                </Content>
            </Layout>
        </Layout>
    )
}

export default LayoutEl
