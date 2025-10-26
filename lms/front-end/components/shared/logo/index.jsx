import { Button } from 'antd'
import { DingdingOutlined } from '@ant-design/icons'

const Logo = ({ size = 32, color='inherit', padding='inherit' }) => {
  return (
    <Button
      className='border-0 shadow-none bg-transparent '
      style={{ 
        fontWeight: 700,
        fontSize: size,
        fontFamily:'bela-semibold',
        color:color,
        padding

        
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