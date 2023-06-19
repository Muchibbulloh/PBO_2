<?php
require_once 'database.php';
require_once 'Pengembalian.php';
$db = new MySQLDatabase();
$pengembalian = new Pengembalian($db);
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
            $result = $pengembalian->get_by_id($id);
        }elseif($kode>0){
            $result = $pengembalian->get_by_kode($kode);
        } else {
            $result = $pengembalian->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new pengembalian
        $pengembalian->kode = $_POST['kode'];
        $pengembalian->tgl_pengembalian = $_POST['tgl_pengembalian'];
        $pengembalian->id_anggota = $_POST['id_anggota'];
        $pengembalian->id_buku = $_POST['id_buku'];
        $pengembalian->id_petugas = $_POST['id_petugas'];
       
        $pengembalian->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Pengembalian created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Pengembalian not created.';
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
        $pengembalian->kode = $_PUT['kode'];
        $pengembalian->tgl_pengembalian = $_PUT['tgl_pengembalian'];
        $pengembalian->id_anggota = $_PUT['id_anggota'];
        $pengembalian->id_buku = $_PUT['id_buku'];
        $pengembalian->id_petugas = $_PUT['id_petugas'];
        if($id>0){    
            $pengembalian->update($id);
        }elseif($kode<>""){
            $pengembalian->update_by_kode($kode);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Pengembalian updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Pengembalian update failed.';
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
            $pengembalian->delete($id);
        }elseif($kode>0){
            $pengembalian->delete_by_kode($kode);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Pengembalian deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Pengembalian delete failed.';
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