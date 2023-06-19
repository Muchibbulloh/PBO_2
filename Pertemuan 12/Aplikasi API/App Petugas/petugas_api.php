<?php
require_once 'database.php';
require_once 'Petugas.php';
$db = new MySQLDatabase();
$petugas = new Petugas($db);
$id=0;
$kode=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kode'])){
            $kode = $_GET['kode'];
        }
        if($id>0){    
            $result = $petugas->get_by_id($id);
        }elseif($kode>0){
            $result = $petugas->get_by_kode($kode);
        } else {
            $result = $petugas->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new petugas
        $petugas->kode = $_POST['kode'];
        $petugas->nama = $_POST['nama'];
        $petugas->telepon = $_POST['telepon'];
        $petugas->alamat = $_POST['alamat'];
        $petugas->jk = $_POST['jk'];
       
        $petugas->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Petugas created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Petugas not created.';
        }
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'PUT':
        // Update an existing data
        $_PUT = [];
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kode'])){
            $kode = $_GET['kode'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $petugas->kode = $_PUT['kode'];
        $petugas->nama = $_PUT['nama'];
        $petugas->telepon = $_PUT['telepon'];
        $petugas->alamat = $_PUT['alamat'];
        $petugas->jk = $_PUT['jk'];
        if($id>0){    
            $petugas->update($id);
        }elseif($kode<>""){
            $petugas->update_by_kode($kode);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Petugas updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Petugas update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kode'])){
            $kode = $_GET['kode'];
        }
        if($id>0){    
            $petugas->delete($id);
        }elseif($kode>0){
            $petugas->delete_by_kode($kode);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Petugas deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Petugas delete failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    default:
        header("HTTP/1.0 405 Method Not Allowed");
        break;
    }
$db->close()
?>