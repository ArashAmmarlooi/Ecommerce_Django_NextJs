'use client'
import { FormEvent } from 'react'

import React, { useState, useEffect, useRef } from "react";
import Link from "next/link";
import Image from 'next/image';
import styles from './register.module.scss';
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





const Register = () => {
    const [formData, setFormData] = useState({
        username: '',
        email: '',
        password: '',
    });
    function onsubmit(event: FormEvent<HTMLFormElement>) {
        event.preventDefault();
        const formdata = new FormData(event.currentTarget);
    }
    useEffect(() => {
        let closefilter = document.querySelector('.filtercomp_closefilter__EZ3kb')

    }, [])
    return (
        <div className={styles.wrapper}>
            <h3>ثبت نام</h3>
            <form onSubmit={onsubmit}>

                {/* <div className={styles.inputbox}>
                    <input type="text" name='username'
                        placeholder="نام کاربری خود را وارد کنید..."
                        value={formData.name}
                        onChange={handleChange}
                        required />
                </div>
                <div className={styles.inputbox}>
                    <input
                        value={formData.name}
                        onChange={handleChange}
                        type="email"
                        name='email'
                        placeholder="ایمیل خود را وارد کنید..."
                        required />
                </div>
                <div className={styles.inputbox}>
                    <input type="password"
                        name='password'
                        placeholder="رمز عبور خود را وارد کنید..."
                        value={formData.name}
                        onChange={handleChange}
                        required />
                </div>
                <div className={styles.inputbox}>
                    <input type="password"
                        value={formData.name}
                        onChange={handleChange}
                        name='password'
                        placeholder="تکرار رمز عبور..."
                        required />
                </div> */}
                <div className={styles.policy}>
                    <input type="checkbox" />
                    <h3>همه قوانین را میپذیرم</h3>
                </div>
                <div className={`${styles.inputbox} ${styles.button}`}>
                    <button type="submit">ثبت نام کنید</button>
                </div>
                <div className={styles.text}>
                    <h3>آیا قبلا ثبت نام کرده اید؟ <a href="#">وارد شوید</a></h3>
                </div>
            </form>
        </div>
    );
}



export default Register;