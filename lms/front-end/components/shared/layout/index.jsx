'use client'

import {Layout, Button, Menu} from 'antd'
import Logo from '../logo/index'
import {useState} from 'react'
import Link from 'next/link'
const {Sider, Content, Header}=Layout
const {Item} =Menu
import {DashboardOutlined, VideoCameraOutlined, PicCenterOutlined} from '@ant-design/icons'



// In antdesign there is already Layout defined, so we wrote here LayoutEl

const LayoutEl = ({children})=>{  //we destructure children, it will hold the code we wrote in between layout
    const [open, setOpen]=useState(true)

    
    // array of objects menus
    const menus=[
        {
            label:'Dashboard',
            href:'/admin',
            icon:<DashboardOutlined/>
        },
        {
            label:'Courses',
            href:'/admin/courses',
            icon:<VideoCameraOutlined/>
        },
    ]
    return(
        <Layout>    
            
            <Sider className='min-h-screen' trigger={null} collapsible collapsed={open}>
        
                <Menu theme="dark">
                    {
                        menus.map((item,index)=>(
                        <Item key={index} icon={item.icon}>
                            <Link href={item.href}>{item.label}</Link>
                        </Item>
                        ))
                    }
                </Menu>
            </Sider>


            <Layout>
            <Header className="!bg-white flex px-6 justify-between items-center">
                <div>
                     <Logo size={32}/>
                </div>
              <div>
              <Button 
                onClick={()=>setOpen(!open)} 
                icon={<PicCenterOutlined />}
                style={{
                    width:40,
                    height:40
                }}
              
              />
            
          
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
