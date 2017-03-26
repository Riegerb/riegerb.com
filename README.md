# Source Code Repository for [riegerb.com](http://riegerb.com)   
    
__Development__    
build  
```sh  
pelican --relative-urls content  
```  
   
run server (localhost)   
```sh
cd output && python -m pelican.server   
```  
   
__Deployment to riegerb.com__  
publish w/ production URL (internal) routing and upload to [AWS S3](http://riegerb.com.s3-website-us-west-2.amazonaws.com)  
```sh
make s3_upload
```
   
__Misc. Notes__  
- contact form uses [Formspree](https://formspree.io/) to implement captcha  
