/** @type {import('next').NextConfig} */
const nextConfig = {
    env: {
        NEXT_PUBLIC_COPILOTKIT_BACKEND_URL: process.env.NEXT_PUBLIC_COPILOTKIT_BACKEND_URL || 'http://agent:8000'
    },
    async rewrites() {
        return [
            {
                source: '/api/copilotkit/:path*',
                destination: 'http://agent:8000/copilotkit/:path*',
            },
        ]
    }
}