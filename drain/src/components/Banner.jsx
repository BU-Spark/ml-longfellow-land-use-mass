import './Banner.css';
import logo from '../assets/logo.png';

const Banner = () => {
    return (
        <div className="banner">
            <img src={logo} alt="Logo" className="banner-logo" />
            <h1 className="banner-text">Longmeadow Historical Society</h1>
        </div>
    );
};

export default Banner;
