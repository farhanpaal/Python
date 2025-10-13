import { Button } from 'antd'
import { DingdingOutlined } from '@ant-design/icons'

const Logo = ({ size = 32 }) => {
  return (
    <Button
      className='border-0 shadow-none '
      style={{ 
        fontWeight: 700,
        fontSize: size,
        fontFamily:'bela-semibold'
        
      }}
      icon={
         
          <DingdingOutlined className="text-rose-600" />
    
      }
    >
      LMS
    </Button>
  )
}

export default Logo