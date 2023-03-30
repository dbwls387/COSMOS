import axios from "axios";
import { useEffect } from "react"
import { useNavigate } from "react-router";
import { useRecoilState } from "recoil";
import { userState } from "../../recoil/states/UserState";

declare const window: typeof globalThis & {
    Kakao: any;
  };
export default function Logout(){
    const navigate = useNavigate();
    // userState recoil
    const [loginUser, setLoginUser] = useRecoilState(userState)
    // 페이지 들어왔을 때 로그아웃되게
    useEffect(()=>{
      console.log('로구아웃')
      axios.get((`/api/accounts/logout/${loginUser.seq}`),
      {
        headers:{
          Authorization : 'baerer ' + loginUser.acToken
        }
      }
          ).then((res)=>{
            console.log(res)
            setLoginUser({...loginUser,acToken:'',seq:0, isLoggedIn:false, coupleId:"" })
          }
          ).catch((err)=>{
            console.log(err)
          })
        // 카카오 sdk 찾도록 초기화
        if (!window.Kakao.isInitialized()){
            window.Kakao.init(process.env.REACT_APP_KAKAO_LOGIN_JS_SUN)
        }
        window.Kakao.Auth.logout()
          .then(function() {
            alert('logout ok\naccess token -> ' + window.Kakao.Auth.getAccessToken());
            console.log('loggedout')
            navigate('/')
          })
          .catch(function() {
            console.log('Not logged in')
          });
        console.log('로구아웃?', loginUser)
    })
    return(
        <>
        </>
    )
}