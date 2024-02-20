'use client'

import React, { useState, useEffect, useRef } from "react";
import Link from "next/link";
import Image from 'next/image';
import styles from './resfiltersort.module.scss';
import Bar from '../../../public/assets/bar.svg';

// function filterpopup() {
//     let filterwrapper = document.querySelector('.products_filterwrapper__9OMlw') as any;
//     let filterblur = document.querySelector('.filterblur') as any;
//     document.body.style.overflow = 'hidden';
//     filterblur.style.display = 'block'
//     console.log(filterblur);
//     filterwrapper.style.display = 'flex';
// }

// function closefilter() {
//     let filterblur = document.querySelector('.filterblur') as any;
//     let filterwrapper = document.querySelector('.products_filterwrapper__9OMlw') as any;
//     document.body.style.overflow = 'auto';
//     filterblur.style.display = 'none'
//     filterwrapper.style.display = 'none';
// }





const Login = () => {

    useEffect(() => {
        let closefilter = document.querySelector('.filtercomp_closefilter__EZ3kb')

    }, [])
    return (
        <div className={styles.resmenu}>
            Login
        </div>
    );
}



export default Login;