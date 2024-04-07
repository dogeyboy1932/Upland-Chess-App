import { RotatingLines } from "react-loader-spinner";


function BasicExample() {
  return (
    <>
        {/* <Spinner animation="border" role="status">
            <span className="visually-hidden">Loading...</span>
        </Spinner> */}

        <RotatingLines
            strokeColor="grey"
            strokeWidth="5"
            animationDuration="0.75"
            width="96"
            visible={true}
        />

        <div>
            Hi
        </div>
    </>
  );
}

export default BasicExample;