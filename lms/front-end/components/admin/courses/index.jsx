import Layout from '../../shared/layout'
import { Button } from 'antd'
const Courses = () => {

    const Toolbar = () => {
        return (
            <>
                <Button>
                    New course
                </Button>
                <Button>
                    New course2
                </Button>
            </>
        )
    }

    return (
        <Layout
            title="Courses"
            subtitle="Start your journey by creating courses"
            toolbar={<Toolbar />}
        >
            <h1>Welcome to courses</h1>
        </Layout>
    )
}

export default Courses