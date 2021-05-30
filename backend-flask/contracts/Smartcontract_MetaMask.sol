pragma solidity >=0.7.0 <0.9.0;

contract SmartContactsongo {

    uint256 number;


    function store(uint256 num) public {
        number = num;
    }

    function retrieve() public view returns (uint256){
        return number;
    }
    
    function buy_coin(uint256 num2) public returns (uint256){
        number = number + num2;
        return number;
    }
    
    function sell_coin(uint256 num3) public returns (uint256){
        number = number - num3;
        return number;
    }
}