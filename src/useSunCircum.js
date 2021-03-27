import { useState, useEffect } from 'react';
import axios from 'axios';

const useSunCircum = () => {
    const [pi, setPi] = useState('');
    const [sunCircum, setSunCircum] = useState(0);
    const sunRadius = 696340;
    useEffect(() => {
        setSunCircum(2*parseFloat(pi)*sunRadius)
    }, [pi])

    const getPi = async () => {
        const res = await axios.get(`http://localhost:5000/getPI`)
            .then(function (response) {
                if (response.status == 200) {
                    console.log(response.data.data)
                    setPi(response.data.data)

                }
            })
            .catch(err => console.error(err))
    
    }

    return [pi, sunCircum, getPi]
}

export default useSunCircum;