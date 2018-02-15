import React from 'react';

import Footer from '../../component/Common/Footer';
import NavHeader from '../../component/Common/NavHeader';

export default class Index extends React.Component {
  render() {
    return (
      <div className="body">
        <NavHeader />
        <Footer />
      </div>
    );
  }
}
