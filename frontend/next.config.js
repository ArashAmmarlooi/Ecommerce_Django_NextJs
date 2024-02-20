const path = require('path')
const withImages = require('next-images');
module.exports = withImages();

module.exports = {
    sassOptions: {
        includePaths: [path.join(__dirname, 'styles')],
        // prependData: `@import "global.module.scss";`
    },
    distDir: '.next',

    images: {
        domains: ["185.10.75.122"],
        // formats: ["image/webp"],

        // path: "/_next/image",
        loader: "default",
        // disableStaticImages: false,
    },
    env: {
        API_URL: 'http://185.10.75.122/api'
    }
}