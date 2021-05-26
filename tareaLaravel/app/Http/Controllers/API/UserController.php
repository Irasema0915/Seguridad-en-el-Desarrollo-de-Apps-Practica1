<?php

namespace App\Http\Controllers\API;

use Illuminate\Http\Request;
use App\Http\Controllers\Controller;
use Illuminate\Support\Str;
use Illuminate\Support\Facades\Auth;

class UserController extends Controller
{
     public function registro(Request $request){
        // o se puede usar con $user = new \App\User();
        $user = new \App\User();
        $user->name     = $request->name;
        $user->email    = $request->email;
        $user->password = bcrypt($request->password);
        if($user->save()){
            return response()->json($user,201);
        }
        return response()->json(null,204);
    }

    public function login(Request $request){
        $credenciales = ["email"=>$request->email, "password"=>$request->password];
        if(Auth::once($credenciales)){
            $token = Str::random(60);
            $request->user()->forceFill([
                'api_token' => hash('sha256', $token),    
            ])->save();
            return response()->json(['token' => $token],201);
        }
        \abort(401);
    }

    
}
